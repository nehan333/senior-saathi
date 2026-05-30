const API_URL = "http://localhost:8000"; // backend will run here

// OCR IMAGE UPLOAD
async function readDoc() {
    document.getElementById("output").innerText = "Processing image...";

    const fileInput = document.createElement("input");
    fileInput.type = "file";
    fileInput.accept = "image/*";

    fileInput.onchange = async () => {
        const file = fileInput.files[0];

        const formData = new FormData();
        formData.append("file", file);

        try {
            const res = await fetch(`${API_URL}/read`, {
                method: "POST",
                body: formData
            });

            const data = await res.json();

            document.getElementById("output").innerText =
                data.text || "No text found";
        } catch (err) {
            document.getElementById("output").innerText =
                "Backend not connected yet";
        }
    };

    fileInput.click();
}

// GOVERNMENT SCHEMES
async function getSchemes() {
    document.getElementById("output").innerText = "Loading schemes...";

    try {
        const res = await fetch(`${API_URL}/schemes`);
        const data = await res.json();

        document.getElementById("output").innerText =
            JSON.stringify(data, null, 2);
    } catch (err) {
        document.getElementById("output").innerText =
            "Backend not connected yet";
    }
}

// TRANSLATION
async function translateText() {
    const text = document.getElementById("output").innerText;

    document.getElementById("output").innerText = "Translating...";

    try {
        const res = await fetch(`${API_URL}/translate`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: text,
                lang: "te" // Telugu (you can change later)
            })
        });

        const data = await res.json();

        document.getElementById("output").innerText =
            data.translated || "No translation";
    } catch (err) {
        document.getElementById("output").innerText =
            "Backend not connected yet";
    }
}