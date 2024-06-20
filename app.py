from flask import Flask, render_template, request, jsonify
import pyodbc
import matplotlib
matplotlib.use('agg')  # Set non-interactive backend
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def test_plot():
    import matplotlib.pyplot as plt
    from io import BytesIO
    import base64

    plt.figure(figsize=(6, 4))
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Test Plot')
    
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)
    plot_img = base64.b64encode(image_stream.getvalue()).decode('utf-8')
    plt.close()

    return f'<img src="data:image/png;base64,{plot_img}">'
if __name__ == '__main__':
    app.run(debug=True)
