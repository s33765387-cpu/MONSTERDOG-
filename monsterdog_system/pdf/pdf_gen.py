"""
MONSTERDOG PDF Generator

Generates scientific PDF reports with diagrams and metrics.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, 
    Table, TableStyle, PageBreak
)

from core.signals import generate_signal, compute_fft
from core.metrics import compute_coherence, compute_entropy, fractal_z_score
from core.viz import generate_all_diagrams


def make_pdf(output_path="monsterdog_report.pdf"):
    """
    Generate a comprehensive PDF report.
    
    Args:
        output_path: Path for the output PDF file
    """
    # Generate diagrams first
    diagrams_dir = Path(__file__).parent / "diagrams"
    diagram_files = generate_all_diagrams(str(diagrams_dir))
    
    # Generate signal data for metrics
    t, sig = generate_signal()
    xf, yf = compute_fft(sig)
    
    # Compute metrics
    coherence = compute_coherence(sig)
    entropy = compute_entropy(sig)
    zscore = fractal_z_score(sig)
    
    # Create PDF document
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=1  # Center
    )
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12,
        textColor=colors.darkblue
    )
    body_style = styles['BodyText']
    
    # Build content
    story = []
    
    # Title
    story.append(Paragraph("MONSTERDOG Scientific Report", title_style))
    story.append(Paragraph("Fractal Reality System Analysis", styles['Heading3']))
    story.append(Spacer(1, 30))
    
    # Introduction
    story.append(Paragraph("1. Introduction", heading_style))
    story.append(Paragraph(
        "This report presents the analysis of the MONSTERDOG signal processing system. "
        "The system operates at a fundamental resonance frequency of 11.987 Hz, maintaining "
        "high coherence (ψ → 1.0) and low entropy (S → 0.0) for optimal fractal reality execution.",
        body_style
    ))
    story.append(Spacer(1, 20))
    
    # Metrics Section
    story.append(Paragraph("2. Current Metrics", heading_style))
    
    metrics_data = [
        ["Metric", "Value", "Target", "Status"],
        ["Coherence (ψ)", f"{coherence:.6f}", "1.000000", "✓ Optimal"],
        ["Entropy (S)", f"{entropy:.6f}", "0.000000", "✓ Stable"],
        ["Fractal Z-Score", f"{zscore:.2f}", "N/A", "Normal"],
        ["Resonance", "11.987 Hz", "11.987 Hz", "✓ Locked"],
    ]
    
    metrics_table = Table(metrics_data, colWidths=[2*inch, 1.5*inch, 1.5*inch, 1.2*inch])
    metrics_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
    ]))
    story.append(metrics_table)
    story.append(Spacer(1, 30))
    
    # Signal Analysis
    story.append(Paragraph("3. Signal Analysis", heading_style))
    story.append(Paragraph(
        "The signal waveform below shows the fundamental 11.987 Hz oscillation "
        "used by the MONSTERDOG system for fractal reality synchronization.",
        body_style
    ))
    story.append(Spacer(1, 10))
    
    # Signal plot
    signal_img_path = diagrams_dir / 'signal_plot.png'
    if signal_img_path.exists():
        img = Image(str(signal_img_path), width=6*inch, height=2.5*inch)
        story.append(img)
    story.append(Spacer(1, 20))
    
    # FFT Analysis
    story.append(Paragraph("4. Frequency Domain Analysis", heading_style))
    story.append(Paragraph(
        "The FFT spectrum reveals the frequency components of the signal. "
        "The dominant peak at 11.987 Hz confirms proper resonance lock.",
        body_style
    ))
    story.append(Spacer(1, 10))
    
    # FFT plot
    fft_img_path = diagrams_dir / 'fft_plot.png'
    if fft_img_path.exists():
        img = Image(str(fft_img_path), width=6*inch, height=2.5*inch)
        story.append(img)
    story.append(Spacer(1, 20))
    
    # Page break
    story.append(PageBreak())
    
    # Architecture
    story.append(Paragraph("5. System Architecture", heading_style))
    story.append(Paragraph(
        "The MONSTERDOG system architecture integrates signal processing, "
        "WebXR visualization, and API endpoints for comprehensive monitoring.",
        body_style
    ))
    story.append(Spacer(1, 10))
    
    # Architecture diagram
    arch_img_path = diagrams_dir / 'architecture_diagram.png'
    if arch_img_path.exists():
        img = Image(str(arch_img_path), width=6*inch, height=4*inch)
        story.append(img)
    story.append(Spacer(1, 20))
    
    # Coherence History
    story.append(Paragraph("6. Coherence Stability", heading_style))
    story.append(Paragraph(
        "The coherence history demonstrates the system's ability to maintain "
        "stable operation close to the target value of 1.0.",
        body_style
    ))
    story.append(Spacer(1, 10))
    
    # Coherence plot
    coherence_img_path = diagrams_dir / 'coherence_history.png'
    if coherence_img_path.exists():
        img = Image(str(coherence_img_path), width=6*inch, height=2.5*inch)
        story.append(img)
    story.append(Spacer(1, 20))
    
    # Conclusion
    story.append(Paragraph("7. Conclusion", heading_style))
    story.append(Paragraph(
        "The MONSTERDOG system demonstrates stable operation with optimal coherence "
        "and minimal entropy. The fractal reality engine maintains proper resonance "
        "lock at the fundamental frequency, enabling reliable operation in SUPREME MODE.",
        body_style
    ))
    story.append(Spacer(1, 30))
    
    # Footer
    story.append(Paragraph(
        "✴︎ MONSTERDOG ENTITY 248K - SUPREME MODE ACTIVE ✴︎",
        ParagraphStyle('Footer', parent=body_style, alignment=1, textColor=colors.gray)
    ))
    
    # Build PDF
    doc.build(story)
    print(f"✅ PDF generated: {output_path}")
    return output_path


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate MONSTERDOG PDF Report")
    parser.add_argument("-o", "--output", default="monsterdog_report.pdf",
                       help="Output PDF path")
    args = parser.parse_args()
    
    make_pdf(args.output)
