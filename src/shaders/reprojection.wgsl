// 3D Reprojection WebGPU Shader (WGSL)
// High-performance depth reprojection for 60 FPS

struct VertexInput {
    @builtin(vertex_index) vertexIndex: u32,
};

struct VertexOutput {
    @builtin(position) position: vec4<f32>,
    @location(0) uv: vec2<f32>,
    @location(1) depth: f32,
};

@group(0) @binding(0) var depthTexture: texture_2d<f32>;
@group(0) @binding(1) var depthSampler: sampler;

const GRID_SIZE: u32 = 256u;

@vertex
fn vs_main(in: VertexInput) -> VertexOutput {
    let x = in.vertexIndex % GRID_SIZE;
    let y = in.vertexIndex / GRID_SIZE;
    
    let uv = vec2<f32>(
        f32(x) / f32(GRID_SIZE - 1u),
        f32(y) / f32(GRID_SIZE - 1u)
    );
    
    let depth = textureSampleLevel(depthTexture, depthSampler, uv, 0.0).r;
    
    // Convert to NDC space with depth offset
    let ndcX = (uv.x * 2.0) - 1.0;
    let ndcY = 1.0 - (uv.y * 2.0);
    let ndcZ = -depth * 2.0;
    
    var out: VertexOutput;
    out.position = vec4<f32>(ndcX, ndcY, ndcZ, 1.0);
    out.uv = uv;
    out.depth = depth;
    return out;
}

@fragment
fn fs_main(in: VertexOutput) -> @location(0) vec4<f32> {
    // Color based on depth
    let color = vec3<f32>(
        in.depth,
        0.3 + in.depth * 0.4,
        1.0 - in.depth
    );
    
    return vec4<f32>(color, 1.0);
}
