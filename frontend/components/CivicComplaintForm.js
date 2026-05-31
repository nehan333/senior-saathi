import { useState } from "react";

function CivicComplaintForm() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const submitComplaint = async () => {
    const res = await fetch("http://127.0.0.1:5001/complaint", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text })
    });

    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Civic Complaint Form</h2>

      <textarea
        rows="4"
        cols="40"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Type your complaint..."
      />

      <br />

      <button onClick={submitComplaint}>
        Submit Complaint
      </button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Result:</h3>
          <p><b>Department:</b> {result.department}</p>
          <p><b>Complaint:</b> {result.complaint}</p>
        </div>
      )}
    </div>
  );
}

export default CivicComplaintForm;
