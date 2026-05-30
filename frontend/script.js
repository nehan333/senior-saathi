async function getSchemes() {
    try {
        const response = await fetch("http://127.0.0.1:8000/schemes");
        const data = await response.json();

        document.getElementById("output").innerText =
            JSON.stringify(data, null, 2);
    } catch (error) {
        document.getElementById("output").innerText =
            "Failed to fetch government schemes.";
    }
}

async function readDoc() {
    try {
        const response = await fetch("http://127.0.0.1:8000/ocr");
        const data = await response.json();

        document.getElementById("output").innerText =
            data.text;
    } catch (error) {
        document.getElementById("output").innerText =
            "OCR extraction failed.";
    }
}

function translateText() {
    document.getElementById("output").innerText =
        "Translation Module Ready (Integration Coming Soon)";
}

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
