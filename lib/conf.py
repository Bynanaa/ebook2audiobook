import os

NATIVE = 'native'
DOCKER_UTILS = 'docker_utils'
FULL_DOCKER = 'full_docker'

version = '2.0.0'
min_python_version = (3,10)
max_python_version = (3,12)

requirements_file = os.path.abspath(os.path.join('.','requirements.txt'))

docker_utils_image = 'utils'
gradio_interface_port = 7860
gradio_shared_expire = 72 # hours
concurrency_limit = 8 # or None for unlimited

python_env_dir = os.path.abspath(os.path.join('.','python_env'))
models_dir = os.path.abspath(os.path.join('.','models'))
ebooks_dir = os.path.abspath(os.path.join('.','ebooks'))
processes_dir = os.path.abspath(os.path.join('.','tmp'))
audiobooks_gradio_dir = os.path.abspath(os.path.join('.','audiobooks','gui','gradio'))
audiobooks_host_dir = os.path.abspath(os.path.join('.','audiobooks','gui','host'))
audiobooks_cli_dir = os.path.abspath(os.path.join('.','audiobooks','cli'))

# <<<<<<< HEAD
# Automatically accept the non-commercial license
os.environ['COQUI_TOS_AGREED'] = '1'
os.environ['CALIBRE_TEMP_DIR'] = processes_dir
os.environ['CALIBRE_CACHE_DIRECTORY'] = processes_dir
os.environ['CALIBRE_NO_NATIVE_FILEDIALOGS'] = '1'
os.environ['DO_NOT_TRACK'] = 'true'
os.environ['HUGGINGFACE_HUB_CACHE'] = models_dir
os.environ['TTS_HOME'] = models_dir
os.environ['HF_HOME'] = models_dir
os.environ['HF_DATASETS_CACHE'] = models_dir
os.environ['HF_TOKEN_PATH'] = os.path.join(os.path.expanduser('~'), '.huggingface_token')
os.environ['TTS_CACHE'] = models_dir
os.environ['TORCH_HOME'] = models_dir
os.environ['XDG_CACHE_HOME'] = models_dir

models = {
    "xtts": {
        "url": "https://huggingface.co/drewThomasson/XTTS_v2_backup_model_files/resolve/main/xtts_v2_default_model.zip?download=true",
        "api": "tts_models/multilingual/multi-dataset/xtts_v2",
        "local": os.path.join(models_dir, "tts", "tts_models--multilingual--multi-dataset--xtts_v2"),
        "files": ["config.json", "model.pth", "vocab.json"],
        "zip": "xtts_v2_model.zip"
    },
    "mms": {
        "url": "",
        "api": "tts_models/[lang]/fairseq/vits",
        "local": os.path.join(models_dir, "tts", "tts_models--[lang]--fairseq--vits"),
        "files": ["config.json", "G_100000.pth", "vocab.txt"],
        "zip": ""
    }
}

ebook_formats = ['.epub', '.mobi', '.azw3', 'fb2', 'lrf', 'rb', 'snb', 'tcr', '.pdf', '.txt', '.rtf', 'doc', '.docx', '.html', '.odt', '.azw']
audiobook_format = 'm4b' # or 'mp3'
audio_proc_format = 'wav' # only 'wav' is valid for now

xtts_fine_tuned_voice_actors = {
    "David Attenborough": {
        "zip_file": "https://huggingface.co/drewThomasson/xtts_David_Attenborough_fine_tune/resolve/main/Finished_model_files.zip?download=true",
        "ref_audio": "https://huggingface.co/drewThomasson/xtts_David_Attenborough_fine_tune/resolve/main/ref.wav?download=true"
    },
    "HeadSpace Dude (Without rain)": {
        "zip_file": "https://huggingface.co/drewThomasson/Headspace_dude/resolve/main/Finished_model_files.zip?download=true",
        "ref_audio": "https://huggingface.co/drewThomasson/Headspace_dude/resolve/main/ref_without_background_rain.wav?download=true"
    },
    "HeadSpace Dude (With background rain sounds)": {
        "zip_file": "https://huggingface.co/drewThomasson/Headspace_dude/resolve/main/Finished_model_files.zip?download=true",
        "ref_audio": "https://huggingface.co/drewThomasson/Headspace_dude/resolve/main/ref_with_background_rain.wav?download=true"
    },
    "Blaidd Elden Ring": {
        "zip_file": "https://huggingface.co/drewThomasson/Blaidd_Elden_Ring_xtts_fineTune/resolve/main/Finished_model_files.zip?download=true",
        "ref_audio": "https://huggingface.co/drewThomasson/Blaidd_Elden_Ring_xtts_fineTune/resolve/main/ref.wav?download=true"
    },
    "Bob Odenkirk": {
        "zip_file": "https://huggingface.co/drewThomasson/xtts-finetune-Bob-Odenkirk/resolve/main/Finished_model_files.zip?download=true",
        "ref_audio": "https://huggingface.co/drewThomasson/xtts-finetune-Bob-Odenkirk/resolve/main/ref.wav?download=true"
    },
    "Bryan Cranston": {
        "zip_file": "https://huggingface.co/drewThomasson/Xtts-Finetune-Bryan-Cranston/resolve/main/V2_Xtts-Finetune-Bryan-Cranston/Finished_model_files.zip?download=true",
        "ref_audio": "https://huggingface.co/drewThomasson/Xtts-Finetune-Bryan-Cranston/resolve/main/V2_Xtts-Finetune-Bryan-Cranston/ref_audio_for_v2.wav?download=true"
    },
    "John Butler ASMR": {
        "zip_file": "https://huggingface.co/drewThomasson/xtts-finetune-John-Butler-Author-ASMR-voice/resolve/main/Finished_model_files.zip?download=true",
        "ref_audio": "https://huggingface.co/drewThomasson/xtts-finetune-John-Butler-Author-ASMR-voice/resolve/main/ref%20(2).wav?download=true"
    },
    "Death from Puss and Boots": {
        "zip_file": "https://huggingface.co/drewThomasson/death_from_puss_and_boots_xtts/resolve/main/V2_Denoised_BEST/Finished_model_files.zip?download=true",
        "ref_audio": "https://huggingface.co/drewThomasson/death_from_puss_and_boots_xtts/resolve/main/V2_Denoised_BEST/ref.wav?download=true"
    },
    "Bob Ross": {
        "zip_file": "https://huggingface.co/drewThomasson/Xtts-FineTune-Bob-Ross/resolve/main/Finished_model_files.zip?download=true",
        "ref_audio": "https://huggingface.co/drewThomasson/Xtts-FineTune-Bob-Ross/resolve/main/ref.wav?download=true"
    },
    "John Mulaney": {
        "zip_file": "https://huggingface.co/drewThomasson/xtts_finetune_John_Mulaney/resolve/main/V2_10_epoches_BEST/Finished_model_files.zip?download=true",
        "ref_audio": "https://huggingface.co/drewThomasson/xtts_finetune_John_Mulaney/resolve/main/V2_10_epoches_BEST/ref.wav?download=true"
    },
    "Morgan Freeman": {
        "zip_file": "https://huggingface.co/drewThomasson/Morgan_freeman_xtts_model/resolve/main/7_epoches/model.zip?download=true",
        "ref_audio": "https://huggingface.co/drewThomasson/Morgan_freeman_xtts_model/resolve/main/7_epoches/ref.wav?download=true"
    },
    "Ai explained": {
        "zip_file": "https://huggingface.co/drewThomasson/ai_explained_xtts_model/resolve/main/ai_explained.zip?download=true",
        "ref_audio": "https://huggingface.co/drewThomasson/ai_explained_xtts_model/resolve/main/ref.wav?download=true"
    },
    "Ghost MW2": {
        "zip_file": "https://huggingface.co/drewThomasson/xtts_ghost_MW2_fine_tune/resolve/main/Finished_model_files.zip?download=true",
        "ref_audio": "https://huggingface.co/drewThomasson/xtts_ghost_MW2_fine_tune/resolve/main/ref.wav?download=true"
    }
}
need_to_find_sample_ref_file_xtts_fine_tuned_models = {
    "French ASMR": {
        "zip_file": "https://huggingface.co/drewThomasson/French_ASMR/resolve/main/French%20ASMR.zip?download=true",
        "ref_audio": "INSIDE ZIP?????"
    },

}
