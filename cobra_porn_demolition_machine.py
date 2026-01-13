"""
⚡ TESLA TEXT ZAPPER ⚡
Electrify your text with AC-powered processing!
Pawn Shop Definition Cleaner + NLP Lightning + Electric Erotica
"""

import flet as ft
import re
import random
import string
from collections import Counter

# --- SIMPLE STRING PROCESSING ---
def simple_clean(text: str) -> str:
    """Basic cleanup - remove extra spaces, strip"""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def remove_pawn_shop_junk(text: str) -> str:
    """Clean pawn shop style garbage - sketchy chars & repetitions"""
    # Remove sketchy symbols often found in spam/junk
    text = re.sub(r'[★☆◆◇●○■□▲△▼▽♠♣♥♦]+', '', text)
    # Remove excessive punctuation (pawn shop vibes)
    text = re.sub(r'[!]{2,}', '!', text)
    text = re.sub(r'[?]{2,}', '?', text)
    text = re.sub(r'[$]{2,}', '$', text)
    # Remove ALL CAPS screaming
    words = text.split()
    words = [w.capitalize() if w.isupper() and len(w) > 2 else w for w in words]
    return ' '.join(words)

# --- ADVANCED TEXT PROCESSING ---
def advanced_process(text: str) -> str:
    """Tesla-grade frequency analysis + pattern detection"""
    words = re.findall(r'\b\w+\b', text.lower())
    freq = Counter(words)

    # Find repeated patterns (Tesla loved patterns)
    repeated = [w for w, c in freq.items() if c > 1 and len(w) > 3]

    # Calculate "energy" score (word diversity)
    unique_ratio = len(set(words)) / max(len(words), 1)
    energy = int(unique_ratio * 100)

    result = f"[ENERGY: {energy}%] "
    if repeated:
        result += f"[PATTERNS: {', '.join(repeated[:5])}] "
    return result + text

# --- NLP (NO LLM) ---
def nlp_analyze(text: str) -> dict:
    """Simple NLP: tokenization, POS-lite, sentiment-lite"""
    words = re.findall(r'\b\w+\b', text.lower())
    sentences = re.split(r'[.!?]+', text)

    # Sentiment-lite (positive/negative word lists)
    positive = {'good', 'great', 'excellent', 'amazing', 'love', 'best', 'brilliant', 'genius', 'power', 'energy', 'light', 'free'}
    negative = {'bad', 'terrible', 'awful', 'hate', 'worst', 'fail', 'dark', 'evil', 'steal', 'scam', 'fake'}

    pos_count = sum(1 for w in words if w in positive)
    neg_count = sum(1 for w in words if w in negative)

    # Determine vibe
    if pos_count > neg_count:
        vibe = "⚡ POSITIVE CHARGE"
    elif neg_count > pos_count:
        vibe = "🌑 NEGATIVE CHARGE"
    else:
        vibe = "⚖️ NEUTRAL CURRENT"

    return {
        'words': len(words),
        'sentences': len([s for s in sentences if s.strip()]),
        'avg_word_len': sum(len(w) for w in words) / max(len(words), 1),
        'vibe': vibe,
        'complexity': 'HIGH VOLTAGE' if sum(len(w) for w in words) / max(len(words), 1) > 6 else 'LOW VOLTAGE'
    }

# --- TESLA TRANSFORM ---
def tesla_transform(text: str) -> str:
    """Add Tesla's wisdom to output"""
    quotes = [
        "\"The present is theirs; the future is mine.\" - Nikola Tesla",
        "\"If you want to find the secrets of the universe, think in terms of energy, frequency and vibration.\" - Nikola Tesla",
        "\"Be alone, that is the secret of invention.\" - Nikola Tesla",
        "\"The scientists of today think deeply instead of clearly.\" - Nikola Tesla",
        "\"I do not think there is any thrill that can go through the human heart like that felt by the inventor.\" - Nikola Tesla",
        "\"Let the future tell the truth, and evaluate each one according to his work.\" - Nikola Tesla"
    ]
    return f"{text}\n\n⚡ {random.choice(quotes)}"

# --- ELECTRIC EROTICA GENERATOR ---
def generate_electric_erotica() -> str:
    """Generate steamy electric-themed prose"""
    subjects = ["She", "He", "They", "The stranger", "The scientist", "The inventor"]
    verbs = ["felt", "sensed", "experienced", "surrendered to", "embraced", "was overwhelmed by"]
    sensations = [
        "a surge of current racing through every nerve",
        "the magnetic pull of forbidden attraction",
        "electricity crackling between their fingertips",
        "voltage building in waves of pleasure",
        "sparks dancing across heated skin",
        "an arc of desire bridging the gap between them"
    ]
    settings = [
        "in the dim glow of the laboratory",
        "beneath the humming Tesla coil",
        "as lightning illuminated the night",
        "surrounded by the buzz of transformers",
        "in the charged atmosphere of the workshop",
        "under the flickering fluorescent lights"
    ]
    continuations = [
        "Their breath quickened as the frequency intensified, bodies drawn together like opposite poles.",
        "The resistance was futile—current always finds the path of least resistance to ground.",
        "Amplitude rising, wavelength shortening, the oscillation between them reached resonance.",
        "Like a capacitor fully charged, the release was inevitable and explosive.",
        "The circuit completed, energy flowed freely, illuminating everything it touched.",
        "Two conductors in perfect contact, the heat of their connection could melt copper."
    ]
    closings = [
        "In that moment, they understood why Tesla chose to chase lightning instead of love.",
        "The meter read off the charts. Some things cannot be measured, only felt.",
        "When the power finally cut, they lay in darkness, still glowing.",
        "AC or DC—it didn't matter. This current flowed both ways.",
        "The experiment was a success. Replication would be necessary. Many times.",
        "Edison could never have imagined electricity used quite like this."
    ]

    story = f"""
╔══════════════════════════════════════╗
║     ⚡ ELECTRIC EROTICA ⚡            ║
╚══════════════════════════════════════╝

{random.choice(subjects)} {random.choice(verbs)} {random.choice(sensations)} {random.choice(settings)}.

{random.choice(continuations)}

{random.choice(closings)}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ "The desire for knowledge is electric." ⚡
"""
    return story

# --- MAIN ZAP FUNCTION ---
def zap_text(text: str) -> str:
    """Full processing pipeline"""
    if not text.strip():
        return "⚠️ Feed me text, mortal!"

    # Stage 1: Simple clean
    cleaned = simple_clean(text)
    cleaned = remove_pawn_shop_junk(cleaned)

    # Stage 2: Advanced processing
    processed = advanced_process(cleaned)

    # Stage 3: NLP analysis
    nlp = nlp_analyze(cleaned)

    # Build output
    output = f"""
╔══════════════════════════════════════╗
║       ⚡ TESLA TEXT ZAPPER ⚡         ║
╚══════════════════════════════════════╝

📝 CLEANED TEXT:
{cleaned}

📊 ANALYSIS:
{processed}

🔬 NLP BREAKDOWN:
   Words: {nlp['words']} | Sentences: {nlp['sentences']}
   Avg Word Length: {nlp['avg_word_len']:.1f}
   Complexity: {nlp['complexity']}
   Vibe: {nlp['vibe']}
"""
    return tesla_transform(output)


def main(page: ft.Page):
    page.title = "⚡ Tesla Text Zapper"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.window.width = 700
    page.window.height = 850
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Title
    title = ft.Text(
        "⚡ TESLA TEXT ZAPPER ⚡",
        size=28,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.CYAN_400,
        text_align=ft.TextAlign.CENTER
    )

    # Description
    desc = ft.Text(
        "Electrify your text with AC-powered processing!\n"
        "Simple cleaning → Advanced analysis → NLP breakdown",
        size=14,
        color=ft.Colors.GREY_400,
        text_align=ft.TextAlign.CENTER
    )

    # Definition
    definition = ft.Container(
        content=ft.Text(
            "PAWN SHOP CLEANER: Removes sketchy symbols, excessive punctuation,\n"
            "ALL CAPS SCREAMING, and spam patterns. Tesla approved! ⚡",
            size=12,
            italic=True,
            color=ft.Colors.AMBER_300,
            text_align=ft.TextAlign.CENTER
        ),
        padding=10,
        border=ft.Border(
            left=ft.BorderSide(1, ft.Colors.AMBER_700),
            top=ft.BorderSide(1, ft.Colors.AMBER_700),
            right=ft.BorderSide(1, ft.Colors.AMBER_700),
            bottom=ft.BorderSide(1, ft.Colors.AMBER_700)
        ),
        border_radius=5
    )

    # Input
    input_box = ft.TextField(
        label="Enter text to ZAP",
        multiline=True,
        min_lines=4,
        max_lines=6,
        border_color=ft.Colors.CYAN_700,
        focused_border_color=ft.Colors.CYAN_400,
        width=550
    )

    # Output
    output_box = ft.TextField(
        label="⚡ OUTPUT",
        multiline=True,
        min_lines=12,
        max_lines=15,
        read_only=True,
        border_color=ft.Colors.GREEN_700,
        value="",
        width=550
    )

    def on_submit(e):
        result = zap_text(input_box.value)
        output_box.value = result
        page.update()

    def on_generate_erotica(e):
        result = generate_electric_erotica()
        output_box.value = result
        page.update()

    # Submit button
    submit_btn = ft.FilledButton(
        "⚡ ZAP IT!",
        on_click=on_submit,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.CYAN_700,
            color=ft.Colors.WHITE
        ),
        width=200,
        height=45
    )

    # Erotica generator button
    erotica_btn = ft.FilledButton(
        "🔥 GENERATE EROTICA",
        on_click=on_generate_erotica,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.PINK_700,
            color=ft.Colors.WHITE
        ),
        width=200,
        height=45
    )

    # Layout - centered
    content = ft.Column(
        [
            title,
            desc,
            ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
            definition,
            ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
            input_box,
            ft.Row([submit_btn, erotica_btn], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            output_box
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(content)

if __name__ == "__main__":
    ft.app(target=main)
