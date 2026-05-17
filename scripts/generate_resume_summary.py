#!/usr/bin/env python3
import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
INPUT_HTML = ROOT / "index.html"
OUTPUT_TXT = ROOT / "resume-summary.txt"


def strip_tags(text: str) -> str:
    no_tags = re.sub(r"<[^>]+>", "", text)
    collapsed = re.sub(r"\s+", " ", no_tags).strip()
    return html.unescape(collapsed)


def format_position(text: str) -> str:
    words = text.lower().split()
    acronyms = {
        "ai": "AI",
        "cpu": "CPU",
        "dsp": "DSP",
        "gpu": "GPU",
        "hal": "HAL",
        "sdk": "SDK",
        "tws": "TWS",
    }
    return " ".join(acronyms.get(word, word.capitalize()) for word in words)


def main() -> None:
    src = INPUT_HTML.read_text(encoding="utf-8")

    eyebrow_match = re.search(r"<p class=\"eyebrow\">(.*?)</p>", src, flags=re.S)
    subtitle_match = re.search(r"<p class=\"subtitle\">\s*(.*?)\s*</p>", src, flags=re.S)
    if not eyebrow_match or not subtitle_match:
        raise SystemExit("포지셔닝 섹션을 찾을 수 없습니다.")

    section_match = re.search(
        r"<h2>\s*경력 요약\s*</h2>\s*<div class=\"timeline\">(.*?)</div>\s*</section>",
        src,
        flags=re.S,
    )
    if not section_match:
        raise SystemExit("경력 요약 섹션을 찾을 수 없습니다.")

    timeline_html = section_match.group(1)
    articles = re.findall(r"<article>(.*?)</article>", timeline_html, flags=re.S)

    lines = [
        "[포지셔닝]",
        format_position(strip_tags(eyebrow_match.group(1))),
        strip_tags(subtitle_match.group(1)),
        "",
        "[경력 요약]",
    ]
    for block in articles:
        period = strip_tags(re.search(r"<div class=\"period\">(.*?)</div>", block, flags=re.S).group(1))
        title = strip_tags(re.search(r"<h3>(.*?)</h3>", block, flags=re.S).group(1))
        role = strip_tags(re.search(r"<p class=\"role-meta\">(.*?)</p>", block, flags=re.S).group(1))
        items = re.findall(r"<li(?! class=\"sub-item\")(?:[^>]*)>(.*?)</li>", block, flags=re.S)
        sub_items = re.findall(r"<li class=\"sub-item\">(.*?)</li>", block, flags=re.S)

        lines.append("")
        lines.append(f"- 기간: {period}")
        lines.append(f"  회사/직무: {title}")
        lines.append(f"  {role}")
        lines.append("  주요 내용:")
        for item in items:
            lines.append(f"  - {strip_tags(item)}")
        for item in sub_items:
            lines.append(f"    * {strip_tags(item)}")

    OUTPUT_TXT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"생성 완료: {OUTPUT_TXT}")


if __name__ == "__main__":
    main()
