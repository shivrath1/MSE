from flask import Flask, request, render_template_string
import base64

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Image Viewer</title>
</head>
<body style="font-family: Arial; text-align:center; margin-top:40px;">

    <h2>Load and Display an Image</h2>

    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="image" accept="image/*" required>
        <br><br>
        <button type="submit">Display Image</button>
    </form>

    {% if image %}
        <h3>Uploaded Image</h3>
        <img src="data:image/png;base64,{{ image }}"
             style="max-width:500px; border:2px solid black;">
    {% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    image = None

    if request.method == "POST":
        file = request.files["image"]

        if file:
            image = base64.b64encode(file.read()).decode("utf-8")

    return render_template_string(HTML, image=image)

if __name__ == "__main__":
    app.run(debug=True)