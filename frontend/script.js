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

document
.getElementById("fileInput")
.addEventListener(
    "change",
    uploadImage
);

async function uploadImage(){

    const file =
        document
        .getElementById("fileInput")
        .files[0];

    if(!file) return;

    const formData =
        new FormData();

    formData.append(
        "file",
        file
    );

    try{

        const response =
            await fetch(
                "http://127.0.0.1:8000/ocr",
                {
                    method:"POST",
                    body:formData
                }
            );

        const data =
            await response.json();

        document
        .getElementById("output")
        .innerText =
            data.text;

    }

    catch(error){

        document
        .getElementById("output")
        .innerText =
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
