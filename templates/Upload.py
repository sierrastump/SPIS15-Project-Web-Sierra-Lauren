<!doctype html>
<link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">

<html>
<title>Film Stream</title>

<h1>Upload an image</h1>

<body>
<form enctype="multipart/form-data" action="save_file.py" method="post">
<p>File: <input type="file" name="file"></p>
<p><input type="submit" value="Upload"></p>
</form>
</body>

</html>
