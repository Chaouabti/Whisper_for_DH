import torch
import whisper
import gradio as gr
import tempfile
import os
import json

def load_whisper_model(model_file=None, model_name=None):

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # 1st case : if a personnal model is loaded (.pt)
    if model_file is not None:
        try:
            model_path = model_file.name if hasattr(model_file, 'name') else model_file
            whisper_model = whisper.load_model(model_path, device=device)
            print(f'Model loaded from {model_path}')
            return whisper_model
        
        except Exception as e:
            print(f"An error occurred while loading the model: {e}")
            raise
        
    # 2nd case : standard whisper model selected
    elif model_name is not None:
        try:
            whisper_model = whisper.load_model(model_name, device=device)
            print(f" Whisper model '{model_name}' has been loaded.")
            return whisper_model
        except Exception as e:
            print(f"An error occurred while loading the model: {e}")
            raise
        
    # No model specified
    raise ValueError("Aucun modèle fourni : vous devez soit uploader un fichier .pt, soit choisir un nom de modèle.")


def transcribe(audio_file, model_file, model_name):
    try:
        whisper_model = load_whisper_model(model_file, model_name)
        result = whisper_model.transcribe(audio_file)
        return result['text'], result['segments'], result.get('language', None)
    
    except Exception as e:
        print(f'Erreur pendant la transcription : {e}')
        raise
    
def gradio_transcription(audio_file, model_file, model_name, output_type):
    try:
        text, segments, language = transcribe(audio_file, model_file, model_name)

        if output_type == "Texte":
            # Créer un fichier temporaire texte à télécharger
            fd, text_path = tempfile.mkstemp(suffix=".txt", dir=".")
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write(text)
            return text, text_path, language

        else:  # JSON
            fd, json_path = tempfile.mkstemp(suffix=".json", dir=".")
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(segments, f, ensure_ascii=False, indent=2)
            return json.dumps(segments, ensure_ascii=False, indent=2), json_path, language

    except Exception as e:
        return f"Erreur : {str(e)}", None, None
    
available_models = whisper.available_models()

with gr.Blocks() as demo:
    with gr.Row():
        audio_input = gr.File(label="Fichier audio ou vidéo", type="filepath", file_types=[".mp3", ".mp4", ".mpa", ".m4a", ".wav", ".flac", ".aac", ".ogg"])
        model_file_input = gr.File(label="Modèle personnalisé (.pt)", type="filepath", file_types=[".pt"])
    
    model_dropdown = gr.Dropdown(choices=available_models, label="Modèle Whisper (si aucun fichier .pt)")
    
    output_type = gr.Radio(choices=["Texte", "JSON"], label="Afficher la sortie sous forme de :", value="Texte")

    run_button = gr.Button("Transcrire")

    output_display = gr.Textbox(label="Transcription / Segments JSON", lines=20, interactive=False)
    download_button = gr.File(label="Télécharger le résultat", visible=False)
    language_output = gr.Textbox(label="Langue détectée", interactive=False)

    run_button.click(
        fn=gradio_transcription,
        inputs=[audio_input, model_file_input, model_dropdown, output_type],
        outputs=[output_display, download_button, language_output]
    )

demo.launch(share=True)