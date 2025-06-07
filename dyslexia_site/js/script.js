/* Utility script for accessibility controls */
document.addEventListener('DOMContentLoaded', function () {
    var body = document.body;
    var fontSize = 100; // percentage

    function setFontSize() {
        body.style.fontSize = fontSize + '%';
    }

    document.getElementById('font-plus').addEventListener('click', function () {
        fontSize += 10;
        setFontSize();
    });

    document.getElementById('font-minus').addEventListener('click', function () {
        if (fontSize > 50) {
            fontSize -= 10;
            setFontSize();
        }
    });

    document.getElementById('toggle-dyslexia').addEventListener('click', function () {
        body.classList.toggle('dyslexia-mode');
    });

    document.getElementById('toggle-contrast').addEventListener('click', function () {
        body.classList.toggle('high-contrast');
        body.classList.remove('sepia');
    });

    document.getElementById('toggle-sepia').addEventListener('click', function () {
        body.classList.toggle('sepia');
        body.classList.remove('high-contrast');
    });

    document.getElementById('toggle-gradient').addEventListener('click', function () {
        body.classList.toggle('gradient-guide');
    });

    var speakBtn = document.getElementById('speak-content');
    if (speakBtn) {
        speakBtn.addEventListener('click', function () {
            var msg = new SpeechSynthesisUtterance(document.querySelector('main').innerText);
            window.speechSynthesis.speak(msg);
        });
    }
});
