import svgwrite
from results import res
def generate_svg(languages_percentage, output_file="languages.svg"):
    bar_height = 20
    width = 800
    height = bar_height + 130
    border_radius = 2

    dwg = svgwrite.Drawing(output_file, (width, height))

    x = 0
    y = 0
    label_y = y + 35

    for language, percentage in languages_percentage.items():
        language_width = width * (percentage / 100)
        
        # Color of technologies
        colors = {
            "Python": "#3776AB",
            "JavaScript": "#F0DB4F",
            "HTML": "#E44D26",
            "CSS": "#264DE4",
            "TypeScript": "#007ACC"
        }
        
        # Name plus color dot
        label_x = 40
        dwg.add(dwg.circle(center=(label_x, label_y), r=2, fill=colors[language]))
        dwg.add(dwg.text(language, insert=(label_x + 8, label_y + 5), font_size="12",font_family="Segoe UI",fill="#FFFFFF"))
        # Add a language bar with rounded border
        dwg.add(dwg.rect(insert=(x, y), size=(language_width, bar_height), fill=colors[language], rx=border_radius))


        label_y += 20
        x += language_width

    dwg.save()
    
languages_percentage = {
    "JavaScript": res["JavaScript"],
    "Python": res["Python"],
    "TypeScript": res["TypeScript"],
    "HTML": res["HTML"],
    "CSS": res["CSS"]
}

generate_svg(languages_percentage)
