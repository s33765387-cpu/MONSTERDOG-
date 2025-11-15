// Particle Fragment Shader (GLSL)
// Exogene particle rendering with dynamic color

precision highp float;

varying vec3 vColor;
varying float vAlpha;

void main() {
    // Circular particle shape
    vec2 center = gl_PointCoord - vec2(0.5, 0.5);
    float dist = length(center);
    
    if (dist > 0.5) {
        discard;
    }
    
    // Soft edges
    float alpha = vAlpha * (1.0 - smoothstep(0.3, 0.5, dist));
    
    gl_FragColor = vec4(vColor, alpha);
}
