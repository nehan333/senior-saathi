function speakOutput() {

    const text =
    document.getElementById("output").innerText;

    const speech =
    new SpeechSynthesisUtterance(text);

    const lang =
    document.getElementById("language").value;

    speech.lang = lang;

    speechSynthesis.speak(speech);
}