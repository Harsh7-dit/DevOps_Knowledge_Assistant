import React, { useState, useEffect, useRef } from "react";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const chatRef = useRef(null);

  // 🔥 Auto scroll to bottom
  useEffect(() => {
    chatRef.current?.scrollTo({
      top: chatRef.current.scrollHeight,
      behavior: "smooth"
    });
  }, [messages, loading]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMsg = { sender: "user", text: input };
    setMessages(prev => [...prev, userMsg]);

    const question = input;
    setInput("");
    setLoading(true);

    try {
      const response = await fetch("http://34.239.162.206:8000/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ question })
      });

      const data = await response.json();

      const botMsg = {
        sender: "bot",
        text: data.answer,
        sources: data.sources,
        context: data.context
      };

      setMessages(prev => [...prev, botMsg]);
    } catch (error) {
      console.error(error);
    }

    setLoading(false);
  };

  return (
    <div style={{ maxWidth: "700px", margin: "auto", padding: "20px" }}>
      <h2>DevOps Assistant 🤖</h2>

      {/* 🔥 Chat Container */}
      <div
        ref={chatRef}
        style={{
          height: "450px",
          overflowY: "auto",
          border: "1px solid #ccc",
          padding: "10px",
          borderRadius: "10px",
          background: "#f9f9f9"
        }}
      >
        {messages.map((msg, i) => (
          <div
            key={i}
            style={{
              textAlign: msg.sender === "user" ? "right" : "left",
              margin: "10px 0"
            }}
          >
            <div
              style={{
                background: msg.sender === "user" ? "#007bff" : "#28a745",
                color: "white",
                padding: "10px",
                borderRadius: "10px",
                display: "inline-block",
                maxWidth: "80%",
                wordBreak: "break-word",
                whiteSpace: "pre-wrap"
              }}
            >
              <b>{msg.sender === "user" ? "You" : "Bot"}:</b>
              <p>{msg.text}</p>

              {/* 🔥 Sources */}
              {msg.sources && (
                <div style={{ fontSize: "12px", marginTop: "5px" }}>
                  <b>Sources:</b> {msg.sources.join(", ")}
                </div>
              )}

              {/* 🔥 Collapsible Context */}
              {msg.context && (
                <details style={{ marginTop: "5px", fontSize: "12px" }}>
                  <summary>View Context</summary>
                  <ul>
                    {msg.context.map((c, idx) => (
                      <li key={idx}>
                      <details>
                       <summary>{c.slice(0, 100)}...</summary>
                       <p>{c}</p>
                       </details>
                      </li>
                    ))}
                  </ul>
                </details>
              )}
            </div>
          </div>
        ))}

        {/* 🔥 Typing Animation */}
        {loading && (
          <div style={{ textAlign: "left", margin: "10px 0" }}>
            <div
              style={{
                background: "#28a745",
                color: "white",
                padding: "10px",
                borderRadius: "10px",
                display: "inline-block"
              }}
            >
              Typing<span className="dots"></span>
            </div>
          </div>
        )}
      </div>

      {/* 🔥 Input Section */}
      <div style={{ marginTop: "10px", display: "flex" }}>
        <input
          style={{
            flex: 1,
            padding: "10px",
            borderRadius: "5px",
            border: "1px solid #ccc"
          }}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          placeholder="Ask something..."
        />

        <button
          onClick={sendMessage}
          style={{
            padding: "10px",
            marginLeft: "5px",
            borderRadius: "5px",
            border: "none",
            background: "#007bff",
            color: "white",
            cursor: "pointer"
          }}
        >
          Send
        </button>
      </div>

      {/* 🔥 Typing Animation CSS */}
      <style>{`
        .dots::after {
          content: '';
          animation: dots 1.5s steps(3, end) infinite;
        }

        @keyframes dots {
          0% { content: ''; }
          33% { content: '.'; }
          66% { content: '..'; }
          100% { content: '...'; }
        }
      `}</style>
    </div>
  );
}

export default App;
