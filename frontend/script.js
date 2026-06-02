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
        return;
    }

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

        const data =
            await response.json();

        document
            .getElementById("output")
            .innerText =
            data.text;

    } catch (error) {

        console.error(error);

        document
            .getElementById("output")
            .innerText =
            "OCR extraction failed.";
    }
}


async function translateText() {

    const text =
        document
        .getElementById("output")
        .innerText;

    const language =
        document
        .getElementById("language")
        .value;

    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/translate",
                {
                    method: "POST",
                    headers: {
                        "Content-Type":
                            "application/json"
                    },
                    body: JSON.stringify({
                        text: text,
                        language: language
                    })
                }
            );

        const data =
            await response.json();

        document
            .getElementById("output")
            .innerText =
            data.translated;

    } catch (error) {

        console.error(error);

        document
            .getElementById("output")
            .innerText =
            "Translation failed.";
    }
}


async function speakOutput() {

    const text =
        document.getElementById("output").innerText;

    const language =
        document.getElementById("language").value;

    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/voice",
                {
                    method: "POST",
                    headers: {
                        "Content-Type":
                            "application/json"
                    },
                    body: JSON.stringify({
                        text: text,
                        language: language
                    })
                }
            );

        const data =
            await response.json();

        const audio =
            new Audio(
                `http://127.0.0.1:8000/audio/${data.audio}`
            );

        audio.play();

    }

    catch(error) {

        console.error(error);

        document.getElementById("output").innerText =
            "Voice generation failed.";
    }
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
