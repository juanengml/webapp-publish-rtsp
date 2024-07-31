from flask import Flask, render_template, request, flash, redirect, url_for
import ffmpeg
import multiprocessing

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dicionário para armazenar os processos ativos
active_streams = {}

# Função principal para iniciar o processo FFmpeg
def start_stream(input_url, output_url):
    try:
        ffmpeg.input(input_url).output(output_url, codec='copy', f='rtsp', rtsp_transport='tcp').run(capture_stdout=True, capture_stderr=True)
    except ffmpeg.Error as e:
        # Para simplificação, printa o erro, mas você pode logar ou tratar de outra forma
        print(f"Error: {e.stderr.decode('utf-8')}")

# Rota principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_url = request.form['input_url']
        output_url = request.form['output_url']
        # Criar e iniciar um novo processo para o stream
        stream_process = multiprocessing.Process(target=start_stream, args=(input_url, output_url))
        stream_process.start()
        # Adicionar o processo ao dicionário de streams ativos
        active_streams[stream_process.pid] = {
            'input_url': input_url,
            'output_url': output_url,
            'process': stream_process
        }
        flash(f"Started stream from {input_url} to {output_url}.", "info")
        return redirect(url_for('index'))

    return render_template('index.html', active_streams=active_streams)

# Rota para parar um stream ativo
@app.route('/stop/<int:process_id>', methods=['POST'])
def stop(process_id):
    stream_info = active_streams.get(process_id)
    if stream_info:
        process = stream_info['process']
        # Terminar o processo
        process.terminate()
        process.join()
        active_streams.pop(process_id, None)
        flash(f"Stopped stream from {stream_info['input_url']} to {stream_info['output_url']}.", "success")
    else:
        flash("Stream not found.", "danger")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
