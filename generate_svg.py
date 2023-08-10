import svgwrite
from results import res
def generate_svg(languages_percentage, output_file="languages.svg"):
    bar_height = 28
    width = 800
    height = bar_height 
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
        text = f"{language} {round(percentage, 1)}%"
        label_x = x
       
        #dwg.add(dwg.circle(center=(label_x, label_y), r=2, fill=colors[language]))
        dwg.add(dwg.rect(insert=(x, y), size=(language_width, bar_height), fill=colors[language], rx=border_radius))
        dwg.add(dwg.text(text, insert=(label_x + 3,  17), font_size="13",font_family="Arial",fill="#000000"))
        
        # Add a language bar with rounded border


        label_y += 0
        x += language_width

    dwg.save()
    
languages_percentage = {
    "JavaScript": res["JavaScript"],
    "TypeScript": res["TypeScript"],
    "Python": res["Python"],
    "HTML": res["HTML"],
    "CSS": res["CSS"]
}
sorted_languages_percentage = dict(sorted(languages_percentage.items(), key=lambda item: item[1], reverse=True))

print(sorted_languages_percentage)
generate_svg(sorted_languages_percentage)
