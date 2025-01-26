<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Media on Webpage</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        .media {
            margin-bottom: 20px;
        }
        .media img, .media video, .media iframe {
            max-width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <h1>Adding Different Forms of Media to a Webpage</h1>
    
    <!-- Image -->
    <div class="media">
        <h2>Image</h2>
        <img src="https://via.placeholder.com/600x400" alt="Sample Image">
        <p>This is an example of an image displayed on the webpage.</p>
    </div>
    
    <!-- Video -->
    <div class="media">
        <h2>Video</h2>
        <video controls>
            <source src="sample-video.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <p>This is an example of a video. The video is set to be playable directly on the webpage.</p>
    </div>
    
    <!-- Audio -->
    <div class="media">
        <h2>Audio</h2>
        <audio controls>
            <source src="sample-audio.mp3" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>
        <p>This is an example of an audio file that users can play.</p>
    </div>
    
    <!-- Embedded Content -->
    <div class="media">
        <h2>Embedded Content</h2>
        <iframe 
            src="https://www.youtube.com/embed/dQw4w9WgXcQ" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
        </iframe>
        <p>This is an embedded YouTube video.</p>
    </div>

    <footer>
        <p>© 2025 Media Example Webpage</p>
    </footer>
</body>
</html>
