<!doctype html>
<link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">
<title>Temperature Conversion Results</title>

<h1>Here is your temperature conversion</h1>

<ul>
  <li>Farehheit: {{ showFtemp }} </li>
  <li>Celsius: {{ showCtemp }} </li>
</ul>

<a href='{{ url_for('tempConvert') }}'>Do another conversion</a>

