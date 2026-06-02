<<<<<<< Updated upstream
async function getSchemes() {
    try {
        const response =
            await fetch(
                "http://127.0.0.1:8000/schemes"
            );

        const data =
            await response.json();

        document.getElementById("output").innerText =
            JSON.stringify(data, null, 2);

    } catch (error) {

        console.error(error);

        document.getElementById("output").innerText =
            "Failed to fetch government schemes.";
    }
}


window.addEventListener("DOMContentLoaded", () => {

    const fileInput =
        document.getElementById("fileInput");

    if (fileInput) {

        fileInput.addEventListener(
            "change",
            uploadImage
        );

        console.log("File input connected");
    }

});


async function uploadImage() {

    const file =
        document
        .getElementById("fileInput")
        .files[0];

    if (!file) {
        console.log("No file selected");
        return;
    }

    console.log("Uploading:", file.name);

    const formData =
        new FormData();

    formData.append(
        "file",
        file
    );

    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/ocr",
                {
                    method: "POST",
                    body: formData
                }
            );

        console.log(
            "Response status:",
            response.status
        );

        const data =
            await response.json();

        console.log(
            "OCR Response:",
            data
        );

        document
            .getElementById("output")
            .innerText =
            data.text;

    } catch (error) {

        console.error(
            "OCR Error:",
            error
        );

        document
            .getElementById("output")
            .innerText =
            "OCR extraction failed.";
    }
}


function translateText() {

    document
        .getElementById("output")
        .innerText =
        "Translation Module Ready (Integration Coming Soon)";
}


function speakOutput() {

    const text =
        document
        .getElementById("output")
        .innerText;

    const speech =
        new SpeechSynthesisUtterance(
            text
        );

    const lang =
        document
        .getElementById("language")
        .value;

    speech.lang = lang;

    speechSynthesis.speak(
        speech
    );
}


async function addContact() {

    const name =
        document
        .getElementById("contactName")
        .value;

    const phone =
        document
        .getElementById("contactPhone")
        .value;

    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/contacts",
                {
                    method: "POST",
                    headers: {
                        "Content-Type":
                            "application/json"
                    },
                    body: JSON.stringify({
                        name: name,
                        phone: phone
                    })
                }
            );

        const data =
            await response.json();

        document
            .getElementById("output")
            .innerText =
            JSON.stringify(
                data,
                null,
                2
            );

    } catch (error) {

        console.error(error);

        document
            .getElementById("output")
            .innerText =
            "Failed to add contact.";
    }
}


async function viewContacts() {

    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/contacts"
            );

        const data =
            await response.json();

        document
            .getElementById("output")
            .innerText =
            JSON.stringify(
                data,
                null,
                2
            );

    } catch (error) {

        console.error(error);

        document
            .getElementById("output")
            .innerText =
            "Failed to fetch contacts.";
    }
}


async function sendEmergency() {

    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/emergency",
                {
                    method: "POST"
                }
            );

        const data =
            await response.json();

        document
            .getElementById("output")
            .innerText =
            JSON.stringify(
                data,
                null,
                2
            );

    } catch (error) {

        console.error(error);

        document
            .getElementById("output")
            .innerText =
            "Emergency alert failed.";
    }
}
<<<<<<< Updated upstream
=======
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
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
