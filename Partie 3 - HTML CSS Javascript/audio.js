document.addEventListener('DOMContentLoaded', () => {
    const audio = document.createElement('audio');
    audio.id = 'background-music';
    audio.preload = 'auto';
    audio.loop = true;
    const source = document.createElement('source');
    source.src = '../Images et audios/Mark_Ambor_Belong_Together.mp3';
    source.type = 'audio/mp3';
    audio.appendChild(source);

    document.body.appendChild(audio);
    
    const musicButton = document.createElement('button');
    musicButton.textContent = 'Démarrer la musique';
    musicButton.id = 'start-music-button';
    document.body.appendChild(musicButton);

    musicButton.style.position = 'fixed';
    musicButton.style.left = '80%';
    musicButton.style.transform = 'translateX(-50%)';

    musicButton.addEventListener('click', function() {
        if (audio.paused) {
            audio.play().catch(error => {
                console.log("Erreur de lecture de la musique : ", error);
            });
            musicButton.textContent = 'Arrêter la musique';
        } else {
            audio.pause();
            musicButton.textContent = 'Démarrer la musique';
        }
    });
});