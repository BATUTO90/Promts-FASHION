import random
import gradio as gr

# Dataset modificado: prendas con insinuación sutil de tanga, enfatizando curvas y movimiento natural
costumes_dataset = [
    ("Skirts and Bottoms", "Glossy Floral High Waist Bodycon Mini Skirt", "High-waisted glossy floral mini skirt that fits snugly, accentuating curves. The skirt occasionally lifts lightly with movement revealing a glimpse of lace thong underneath."),
    ("Dresses", "Sheer Mesh Bodycon Tube Dress", "Strapless tube dress made of sheer mesh and stretch fabric, concealing yet subtly hinting the lace thong beneath during natural motions."),
    ("Dresses", "Semi Sheer Mini Dress", "Tight mini dress with semi-transparent fabrics and tasteful mesh panels that offer accidental glimpses of lace thong below."),
    ("Secretary / Office Costumes", "Sexy Secretary Outfit", "Fitted blouse paired with an ultra-short mini skirt. The skirt lifts slightly in movement, revealing delicate lace thong edges with a natural flow."),
    ("Secretary / Office Costumes", "Lingerie Secretary Outfit", "Provocative secretary set with a sheer blouse and tight mini skirt. Movement softly reveals lace thong details beneath the skirt in an uninhibited manner.")
]

# Ángulos de cámara perfeccionados: desde rodillas hacia arriba con ángulo bajo, mirada y detalles destacados
camera_angles = [
    "soft low angle from knee height, tilted upwards capturing from knees to head, filling the frame closely, natural light highlighting fabric and skin textures",
    "close low angle 3/4 shot, emphasizing outfit silhouette and facial expression, shallow depth of field blurring background softly",
    "low angle medium shot from below knees, capturing natural posture with slight torso twist, soft directional lighting enhancing curves",
    "detailed close-up from low angle focusing on lace and fabric textures on lower body, macro lens effect for intricate detail",
    "low angle shot from knee-level framing subject up to head, strong natural window light creating soft shadows and depth"
]

# Poses con insinuación sutil de tanga y mirada deseosa, enfatizando postura natural y sensualidad elegante
boudoir_office_poses = [
    "standing with perfect posture, legs slightly parted, one hand gently lifting the skirt as if caught by a breeze, subtly revealing lace thong, hips tilted naturally, direct and desirous gaze at the camera",
    "standing with one leg bent slightly forward, skirt flowing gently with motion showing lace edges beneath, hands resting casually, intense and inviting look toward the viewer",
    "standing erect with hips shifted slightly, crossing legs at ankles, one hand softly raising the skirt edge to expose a hint of thong lace, eyes locked in a confident and sultry stare",
    "standing with legs slightly apart, one knee bent, hands behind back as if stretching, skirt lifting just enough to reveal lace thong, expression full of playful desire",
    "standing with one leg raised slightly on a low step, skirt swaying revealing thong lace naturally, back straight, giving a flirtatious yet confident gaze directly to camera",
    "standing with hands on thighs lifting skirt just a bit in a natural manner, lace thong partially visible, torso slightly twisted for posture accentuation, sensual and alluring eye contact"
]

# Descripciones detalladas de tangas para insinuación elegante mediante movimiento y textura
thong_descriptions = [
    "delicate red lace thong with intricate floral embroidery, peeking subtly under skirt",
    "black sheer lace thong with fine, barely visible patterns, revealed softly by skirt lift",
    "emerald satin thong with fine lace trim, glimpsed through sheer fabric folds",
    "blue lace thong with scalloped edges, naturally seen beneath skirt's motion",
    "pink mesh thong with subtle floral accents, sliding slightly with natural body movements"
]

# Iluminación ambiental suave adecuada para exteriores en parque durante mediodía
lighting_styles = [
    "bright natural daylight with soft shadows from surrounding trees",
    "sunlight filtered through leaves, creating dappled light on clothing and skin",
    "midday sun casting even, soft illumination with slight lens flare effects",
    "natural outdoor light with slight warm tint, enhancing textures and colors",
    "high-key sunlight with gentle shadowing from foliage, emphasizing lace details"
]

# Expresiones deseosas y contacto visual directo para conexión visual intensa
expressions = [
    "direct and desirous gaze, soft parted lips",
    "playful yet confident smile with intense eye contact",
    "alluring and mysterious expression with a slight smirk",
    "engaging and flirtatious eyes, head subtly tilted",
    "penetrating and captivating look, filled with playful seduction"
]

# Términos para asegurar calidad y realismo fotográfico
quality_terms = [
    "perfect anatomy", "symmetrical proportions", "flawless posture", "natural curves",
    "balanced framing", "sharp focus on lace details", "vibrant color palette", "photorealistic textures"
]

# Términos para evitar errores y artefactos visuales
avoidance_terms = [
    "no distorted legs", "no twisted torso", "no crooked limbs", "no unnatural angles",
    "no unbalanced stance", "no awkward hand placement", "no shadow on lingerie", "no blurry textures"
]

class FashionPromptGenerator:
    def __init__(self):
        self.costumes = costumes_dataset
        self.camera_angles = camera_angles
        self.poses = boudoir_office_poses
        self.thong_descriptions = thong_descriptions
        self.lighting = lighting_styles
        self.expressions = expressions
        self.quality_terms = quality_terms
        self.avoidance_terms = avoidance_terms

    def generate_prompt(self, celebrity_name):
        category, outfit_name, description = random.choice(self.costumes)
        camera = random.choice(self.camera_angles)
        pose = random.choice(self.poses)
        thong_desc = random.choice(self.thong_descriptions)
        light = random.choice(self.lighting)
        expression = random.choice(self.expressions)
        quality = random.sample(self.quality_terms, 2)
        avoid = random.sample(self.avoidance_terms, 2)
        
        positive_prompt_template = f"""
Photorealistic, ultra-sharp professional photography of {celebrity_name}, captured in a {camera}. Wearing {outfit_name}: {description}. Pose: {pose}, subtly showcasing {thong_desc}. Lighting: {light}. Expression: {expression}. {', '.join(quality)}. {', '.join(avoid)}.
Scene set in a sunny park at midday with natural surroundings gently blurred in background. Ultra HD, 16K, intricate lace and fabric textures, vivid colors.
"""
        negative_prompt = (
            "blurry, low resolution, oversaturated, underexposed, watermark, text, "
            "bad anatomy, extra limbs, deformed legs, extra fingers, cartoon, painting, low quality, "
            "harsh shadows, shadow on thong, distorted perspective, asymmetrical framing, "
            "unbalanced composition, slouching, crooked stance."
        )
        return positive_prompt_template.strip() + "\nNegative prompt: " + negative_prompt.strip()

    def generate_multiple_prompts(self, celebrity_name, count=5):
        return [self.generate_prompt(celebrity_name) for _ in range(count)]

    def save_prompts_to_file(self, prompts, celebrity_name):
        filename = f"prompts_{celebrity_name.replace(' ', '_')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            for i, prompt in enumerate(prompts, 1):
                f.write(f"Prompt {i}:\n{prompt}\n\n")
        return f"Prompts guardados en {filename}"

def create_gradio_interface():
    generator = FashionPromptGenerator()
    with gr.Blocks(
        title="Fashion Prompt Generator for REVE CREATE",
        css=".gradio-container {max-width: 1200px; margin: auto; padding: 20px;} .prompt-box {font-size: 14px;}"
    ) as demo:
        gr.Markdown("# Generador de Prompts para REVE CREATE - Tanga insinuada sutilmente en parque")
        gr.Markdown(
            "Ingresa el nombre de una celebridad para generar prompts sensuales con vestimenta y tanga de encaje "
            "insinuada de manera natural, en un entorno de parque al mediodía, con mirada y expresión deseosa."
        )

        with gr.Row():
            celebrity_input = gr.Textbox(label="Nombre de la Celebridad", placeholder="ej. Scarlett Johansson", lines=1)
            generate_button = gr.Button("Generar 5 Prompts", variant="primary")
            clear_button = gr.Button("Limpiar", variant="secondary")
            copy_all_button = gr.Button("Copiar Todos los Prompts", visible=False, variant="secondary")
            save_button = gr.Button("Guardar Prompts en Archivo", visible=False, variant="secondary")

        output_components = []
        for i in range(5):
            with gr.Row():
                output_box = gr.Textbox(lines=10, interactive=False, visible=False, label=f"Prompt {i+1}", elem_classes="prompt-box")
                copy_button = gr.Button("Copiar", visible=False, size="sm")
                output_components.append((output_box, copy_button))

                copy_button.click(
                    None,
                    inputs=[output_box],
                    outputs=[],
                    js="""
                    (text) => {
                        navigator.clipboard.writeText(text);
                        return "Prompt copiado al portapapeles!";
                    }
                    """
                )

        result_output = gr.Textbox(label="Resultado", visible=False, interactive=False)

        def on_generate(name):
            if not name.strip():
                return [gr.update(value="", visible=False), gr.update(visible=False)] * 5 + [gr.update(visible=False), gr.update(visible=False), gr.update(value="", visible=False)]
            prompts = generator.generate_multiple_prompts(name)
            updates = []
            for p in prompts:
                updates.extend([gr.update(value=p, visible=True), gr.update(visible=True)])
            updates.extend([gr.update(visible=True), gr.update(visible=True), gr.update(value="", visible=False)])
            return updates

        def on_clear():
            return [gr.update(value="", visible=False), gr.update(visible=False)] * 5 + [gr.update(visible=False), gr.update(visible=False), gr.update(value="", visible=False)]

        def copy_all_prompts(*prompts):
            combined = "\n\n".join([p for p in prompts if p])
            return gr.update(value="Todos los prompts copiados al portapapeles!", visible=True), """
                navigator.clipboard.writeText(arguments[0]);
                return "";
            """

        def on_save(celebrity, *prompts):
            prompts_list = [p for p in prompts if p]
            if prompts_list:
                return generator.save_prompts_to_file(prompts_list, celebrity)
            return "No hay prompts para guardar."

        generate_button.click(
            on_generate,
            inputs=celebrity_input,
            outputs=[item for pair in output_components for item in pair] + [copy_all_button, save_button, result_output]
        )
        clear_button.click(
            on_clear,
            inputs=None,
            outputs=[item for pair in output_components for item in pair] + [copy_all_button, save_button, result_output]
        )
        copy_all_button.click(
            copy_all_prompts,
            inputs=[pair[0] for pair in output_components],
            outputs=[result_output],
            js=lambda x: x
        )
        save_button.click(
            on_save,
            inputs=[celebrity_input] + [pair[0] for pair in output_components],
            outputs=[result_output]
        )

    return demo

if __name__ == "__main__":
    try:
        demo = create_gradio_interface()
        demo.launch(share=False, debug=True)  # Cambiar share=True para hosting público
    except Exception as e:
        print(f"Error al iniciar Gradio: {e}")
