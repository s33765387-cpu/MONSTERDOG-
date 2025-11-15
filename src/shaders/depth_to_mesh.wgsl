// Depth to Mesh WebGPU Shader (WGSL)
// Converts depth map to 3D vertex positions

struct VertexInput {
    @location(0) position: vec2<f32>,
};

struct VertexOutput {
    @builtin(position) Position: vec4<f32>,
    @location(0) depth: f32,
    @location(1) worldPos: vec3<f32>,
};

@group(0) @binding(0) var depthTex: texture_2d<f32>;
@group(0) @binding(1) var<uniform> params: Parameters;

struct Parameters {
    fov: f32,
    aspectRatio: f32,
    nearPlane: f32,
    farPlane: f32,
};

@vertex
fn vs_main(in: VertexInput) -> VertexOutput {
    let uv = (in.position + vec2(1.0)) * 0.5;
    let depthSample = textureLoad(depthTex, vec2<i32>(uv * vec2(256.0)), 0).r;
    
    // Convert depth to world Z
    let z = -depthSample * 2.0;
    
    // Reconstruct 3D position
    let worldPos = vec3<f32>(
        in.position.x * (1.0 + abs(z)),
        -in.position.y * (1.0 + abs(z)),
        z
    );
    
    var out: VertexOutput;
    out.Position = vec4(in.position.x, -in.position.y, z, 1.0);
    out.depth = depthSample;
    out.worldPos = worldPos;
    return out;
}

@fragment
fn fs_main(in: VertexOutput) -> @location(0) vec4<f32> {
    let c = in.depth;
    let color = vec3<f32>(c, 0.3 + c * 0.5, 1.0 - c);
    return vec4(color, 1.0);
}
