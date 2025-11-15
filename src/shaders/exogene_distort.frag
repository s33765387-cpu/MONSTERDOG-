// EXOGENE_DISTORT Fragment Shader (GLSL)
// Dynamic distortion based on entropy, gradient, and vacuum metrics

precision highp float;

uniform sampler2D videoTex;
uniform float entropy;
uniform float gradient;
uniform float vacuum;
varying vec2 vUV;

void main() {
    vec2 uv = vUV;
    
    // Distortion controlled by entropy + vacuum
    float d = sin(uv.y * 10.0 + entropy * 2.0) * 0.01;
    uv.x += d * vacuum;

    // Vertical deformation by gradient
    uv.y += cos(uv.x * 12.0 + gradient * 3.0) * 0.01;

    // Render texture
    vec3 col = texture2D(videoTex, uv).rgb;

    // Exogene color accentuation
    col.r += entropy * 0.1;
    col.b += vacuum * 0.05;

    gl_FragColor = vec4(col, 1.0);
}
