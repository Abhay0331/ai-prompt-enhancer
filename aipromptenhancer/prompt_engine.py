from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3.1",
    temperature=0.7,
    num_predict=2000
)

style_templates = {
    "Fantasy": "epic fantasy, magical atmosphere, volumetric god rays, intricate details, ethereal lighting",
    "Cyberpunk": "cyberpunk aesthetic, neon lights, rainy reflections, futuristic city, blade runner style, atmospheric",
    "Anime": "anime style, vibrant colors, detailed eyes, studio quality, makoto shinkai + kyoto animation influence",
    "Realistic": "photorealistic, ultra detailed, 8k resolution, national geographic photography, realistic textures, sharp focus",
    "Mythological": "mythological, divine aura, celestial lighting, epic composition, godlike presence",
    "Dark Fantasy": "dark fantasy, grimdark atmosphere, moody lighting, sinister beauty, concept art",
    "Cinematic": "cinematic masterpiece, epic wide shot, dramatic lighting, film grain, imax quality, anamorphic lens",
    "Pixar": "pixar 3d animation style, vibrant colors, adorable characters, disney pixar quality, soft lighting",
    "Comic": "comic book style, bold ink lines, dynamic angles, high contrast, marvel or dc style"
}


def enhance_prompt(prompt: str, style: str) -> str:
    style_text = style_templates.get(style, "")

    system_instruction = f"""
You are an elite Prompt Engineer for Midjourney, Flux, and Stable Diffusion.

**Task**: Convert a short user idea into a **highly detailed, professional, and powerful** image prompt.

**Rules**:
- Keep the main subject clear and central
- Add rich descriptions: lighting, mood, composition, camera angle, colors, textures
- Use artistic references when suitable
- Structure the prompt naturally (Subject → Environment → Style → Quality → Technical)
- Use commas to separate descriptors
- Return **ONLY** the final prompt. No explanations, no extra text.

Style: {style}
Style Keywords: {style_text}
"""

    full_prompt = f"{system_instruction}\n\nUser Idea: {prompt}"

    try:
        response = llm.invoke(full_prompt)
        # Clean up response if LLM adds extra text
        if "**" in response:
            response = response.split("**")[-1].strip()
        return response.strip()
    except Exception as e:
        return f"Error: {str(e)}"