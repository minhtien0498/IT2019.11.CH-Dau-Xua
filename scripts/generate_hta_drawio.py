#!/usr/bin/env python3
"""Tạo các file Draw.io có thể chỉnh sửa cho chín sơ đồ HTA của Dấu Xưa."""

from __future__ import annotations

import copy
import xml.etree.ElementTree as ET
from pathlib import Path

from generate_hta_diagrams import DIAGRAMS


ROOT_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT_DIR / "docs" / "02-report" / "diagrams" / "drawio"

PREMIUM = {
    "slug": "hta-premium",
    "goal": ["0. Hoàn thành", "Premium Historical Tour"],
    "steps": [
        ["1. Chọn", "địa điểm"],
        ["2. Xem các", "tuyến"],
        ["3. Chọn", "tuyến"],
        ["4. Xem trước", "nội dung"],
        ["5. Kiểm tra", "trạng thái mua"],
        ["6. Chọn", "thời lượng"],
        ["7. Đi tới", "điểm hiện tại"],
        ["8. Mở", "trải nghiệm"],
        ["9. Điểm", "tiếp theo"],
        ["10. Hoàn thành", "tuyến"],
        ["11. Xem", "tóm tắt"],
    ],
    "child_groups": [
        {
            "anchor": 5,
            "children": [["5.1 Đã mua"], ["5.2 Chọn mua", "và thanh toán"]],
        },
        {
            "anchor": 8,
            "children": [
                ["8.1 Nghe", "lời kể"],
                ["8.2 Âm thanh không gian", "hoặc rung nếu muốn"],
                ["8.3 AR nếu khả dụng", "hoặc phương án thay thế"],
            ],
        },
    ],
    "notes": [["Lặp bước 7–9 cho đến khi hết tuyến tham quan"]],
    "plan": "Plan 0: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 (lặp 7–9) → 10 → 11",
    "premium": True,
}


def normalized_diagrams() -> list[dict[str, object]]:
    diagrams: list[dict[str, object]] = []
    for source in DIAGRAMS:
        item = copy.deepcopy(source)
        item["child_groups"] = [
            {"anchor": item.pop("anchor"), "children": item.pop("children")}
        ]
        item["notes"] = []
        item["premium"] = False
        diagrams.append(item)
    diagrams.append(PREMIUM)
    return diagrams


def label(lines: list[str]) -> str:
    return "<br>".join(lines)


def add_vertex(
    root: ET.Element,
    cell_id: str,
    value: str,
    style: str,
    x: float,
    y: float,
    width: float,
    height: float,
) -> None:
    cell = ET.SubElement(
        root,
        "mxCell",
        {"id": cell_id, "value": value, "style": style, "vertex": "1", "parent": "1"},
    )
    ET.SubElement(
        cell,
        "mxGeometry",
        {
            "x": f"{x:.1f}",
            "y": f"{y:.1f}",
            "width": f"{width:.1f}",
            "height": f"{height:.1f}",
            "as": "geometry",
        },
    )


def add_junction(root: ET.Element, cell_id: str, x: float, y: float) -> None:
    """Add an invisible routing point so connector buses stay clear of boxes."""
    add_vertex(
        root,
        cell_id,
        "",
        "ellipse;html=1;fillOpacity=0;strokeOpacity=0;opacity=0;"
        "resizable=0;movable=0;deletable=0;",
        x - 0.5,
        y - 0.5,
        1,
        1,
    )


def add_straight_edge(root: ET.Element, cell_id: str, source: str, target: str) -> None:
    edge = ET.SubElement(
        root,
        "mxCell",
        {
            "id": cell_id,
            "style": "edgeStyle=none;rounded=0;html=1;endArrow=none;endFill=0;"
            "strokeWidth=2;strokeColor=#64748B;",
            "edge": "1",
            "parent": "1",
            "source": source,
            "target": target,
        },
    )
    ET.SubElement(edge, "mxGeometry", {"relative": "1", "as": "geometry"})


def add_connector_bus(
    root: ET.Element,
    prefix: str,
    source: str,
    source_x: float,
    targets: list[tuple[str, float]],
    bus_y: float,
) -> None:
    """Connect one source to several targets through a shared horizontal bus."""
    bus_xs = sorted({round(x, 4) for x in [source_x, *(x for _, x in targets)]})
    junctions: dict[float, str] = {}
    for index, x in enumerate(bus_xs, start=1):
        junction_id = f"{prefix}-junction-{index}"
        junctions[x] = junction_id
        add_junction(root, junction_id, x, bus_y)

    add_straight_edge(
        root,
        f"{prefix}-source",
        source,
        junctions[round(source_x, 4)],
    )
    for index, (left, right) in enumerate(zip(bus_xs, bus_xs[1:]), start=1):
        add_straight_edge(
            root,
            f"{prefix}-bus-{index}",
            junctions[left],
            junctions[right],
        )
    for index, (target, target_x) in enumerate(targets, start=1):
        add_straight_edge(
            root,
            f"{prefix}-target-{index}",
            junctions[round(target_x, 4)],
            target,
        )


def page_name(index: int, item: dict[str, object]) -> str:
    if index <= 8:
        return f"HTA {index} - M{index}"
    return "HTA 9 - Premium Historical Tour"


def build_diagram(index: int, item: dict[str, object]) -> ET.Element:
    diagram = ET.Element(
        "diagram",
        {"id": f"hta-{index}-{item['slug']}", "name": page_name(index, item)},
    )
    model = ET.SubElement(
        diagram,
        "mxGraphModel",
        {
            "dx": "1600",
            "dy": "900",
            "grid": "1",
            "gridSize": "10",
            "guides": "1",
            "tooltips": "1",
            "connect": "1",
            "arrows": "1",
            "fold": "1",
            "page": "1",
            "pageScale": "1",
            "pageWidth": "1600",
            "pageHeight": "900",
            "math": "0",
            "shadow": "0",
        },
    )
    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})

    premium = bool(item.get("premium"))
    goal_style = (
        "rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;"
        if premium
        else "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"
    ) + "strokeWidth=3;fontFamily=Arial;fontSize=20;fontStyle=1;align=center;verticalAlign=middle;"
    step_style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;strokeWidth=2;fontFamily=Arial;fontSize=16;align=center;verticalAlign=middle;"
    child_style = (
        "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;"
        if premium
        else "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;"
    ) + "strokeWidth=2;fontFamily=Arial;fontSize=15;align=center;verticalAlign=middle;"
    note_style = "rounded=0;whiteSpace=wrap;html=1;fillColor=none;strokeColor=none;fontFamily=Arial;fontSize=15;fontColor=#334155;align=center;verticalAlign=middle;"
    plan_style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#CBD5E1;dashed=1;fontFamily=Arial;fontSize=16;fontStyle=2;fontColor=#334155;align=center;verticalAlign=middle;"

    add_vertex(root, "goal", label(item["goal"]), goal_style, 500, 30, 600, 80)

    steps = item["steps"]
    count = len(steps)
    margin, gap = 30.0, 18.0
    step_width = (1600 - 2 * margin - gap * (count - 1)) / count
    step_centers: list[float] = []
    for step_index, lines in enumerate(steps, start=1):
        x = margin + (step_index - 1) * (step_width + gap)
        step_centers.append(x + step_width / 2)
        add_vertex(root, f"step-{step_index}", label(lines), step_style, x, 190, step_width, 80)

    add_connector_bus(
        root,
        "goal-bus",
        "goal",
        800,
        [(f"step-{step_index}", center) for step_index, center in enumerate(step_centers, start=1)],
        150,
    )

    groups = item["child_groups"]
    group_count = len(groups)
    group_band_width = 1500 / group_count
    for group_index, group in enumerate(groups, start=1):
        children = group["children"]
        child_width, child_gap = (245.0, 25.0) if len(children) <= 3 else (210.0, 18.0)
        span = len(children) * child_width + (len(children) - 1) * child_gap
        anchor_center = step_centers[int(group["anchor"]) - 1]
        band_left = 50 + (group_index - 1) * group_band_width
        band_right = band_left + group_band_width
        start_x = min(max(anchor_center - span / 2, band_left), band_right - span)
        child_targets: list[tuple[str, float]] = []
        for child_index, lines in enumerate(children, start=1):
            child_id = f"child-{group_index}-{child_index}"
            x = start_x + (child_index - 1) * (child_width + child_gap)
            add_vertex(root, child_id, label(lines), child_style, x, 400, child_width, 76)
            child_targets.append((child_id, x + child_width / 2))
        add_connector_bus(
            root,
            f"child-bus-{group_index}",
            f"step-{group['anchor']}",
            anchor_center,
            child_targets,
            350,
        )

    for note_index, lines in enumerate(item.get("notes", []), start=1):
        add_vertex(root, f"note-{note_index}", label(lines), note_style, 500, 535, 600, 45)

    add_vertex(root, "plan", str(item["plan"]), plan_style, 100, 660, 1400, 65)
    return diagram


def new_mxfile() -> ET.Element:
    return ET.Element(
        "mxfile",
        {
            "host": "app.diagrams.net",
            "modified": "2026-09-19T00:00:00.000Z",
            "agent": "Codex",
            "version": "24.7.17",
            "type": "device",
            "compressed": "false",
        },
    )


def write_xml(path: Path, root: ET.Element) -> None:
    ET.indent(root, space="  ")
    tree = ET.ElementTree(root)
    tree.write(path, encoding="utf-8", xml_declaration=True)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    diagrams = normalized_diagrams()

    master = new_mxfile()
    for index, item in enumerate(diagrams, start=1):
        page = build_diagram(index, item)
        master.append(copy.deepcopy(page))

        individual = new_mxfile()
        individual.append(page)
        output = OUTPUT_DIR / f"{item['slug']}.drawio"
        write_xml(output, individual)
        print(f"Generated {output.relative_to(ROOT_DIR)}")

    master_path = OUTPUT_DIR / "HTA_Dau_Xua.drawio"
    write_xml(master_path, master)
    print(f"Generated {master_path.relative_to(ROOT_DIR)} with {len(diagrams)} pages")


if __name__ == "__main__":
    main()
