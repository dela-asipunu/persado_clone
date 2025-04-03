"use client";
import Footer from '@/components/Footer';
import Navbar from '@/components/Navbar';
import Link from 'next/link';
import { useState } from "react";

export default function Prompt() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    
    try {
      const res = await fetch("http://localhost:8000/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ 
          user_id:"12345", // Replace with actual user ID
          input_text: prompt,
         }),
      });

      if (!res.ok) {
        throw new Error("Failed to fetch response");
      }

      const data = await res.json();
      setResponse(data.response);
    } catch (err) {
      
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
        <Navbar />
      <h1 className="text-2xl font-bold mb-4">Ask Our AnansAI for strategies for your business or any ideas</h1>

      <form onSubmit={handleSubmit} className="w-full max-w-md">
        <textarea
          className="w-full p-2 border rounded-md"
          rows="4"
          placeholder="Enter your prompt..."
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          required
        />
        
        <button
          type="submit"
          className="mt-2 w-full bg-blue-600 text-white p-2 rounded-md hover:bg-blue-700"
          disabled={loading}
        >
          {loading ? "Generating..." : "Send Prompt"}
        </button>
      </form>
      <div className="text-center mt-10">
            <Link
                  href="/"
                  className="px-6 py-3 bg-primary text-white rounded-lg hover:bg-secondary transition-all duration-300"
                >
                  Back to Home
                </Link>
        </div>

      {error && <p className="text-red-500 mt-2">{error}</p>}

      {response && (
        <div className="mt-4 p-4 bg-white rounded-md shadow-md">
          <h2 className="font-semibold">AI Response:</h2>
          <p className='mt-2 whitespace-pre-line'>{response}</p>
        </div>
      )}
      <Footer />
    </div>
  );
}
