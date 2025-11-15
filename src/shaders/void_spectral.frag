// VOID_SPECTRAL Fragment Shader (GLSL)
// Spectralization and FFT-like visual effects

precision highp float;

uniform sampler2D videoTex;
uniform float coherence;
uniform float density;
varying vec2 vUV;

void main() {
    vec2 uv = vUV;

    // Spectral effect (rainbow)
    vec3 col = texture2D(videoTex, uv).rgb;
    float spec = sin(uv.x * 50.0) * coherence + density * 2.0;

    // Color modulation
    col.r = col.r + spec * 0.05;
    col.g = col.g + sin(spec) * 0.03;
    col.b = col.b + pow(spec, 2.0) * 0.02;

    gl_FragColor = vec4(col, 1.0);
}
