import React, { useState } from 'react'

export default function App() {
  const [status, setStatus] = useState('')

  async function health() {
    const res = await fetch('/api/health')
    const js = await res.json()
    setStatus(JSON.stringify(js))
  }

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-2xl font-semibold mb-4">IAM CaaS Dashboard (Starter)</h1>
      <div className="space-y-4">
        <button onClick={health} className="px-4 py-2 bg-black text-white rounded">
          Test API Health
        </button>
        <pre className="bg-white p-3 rounded border">{status || 'Click the button to call API'}</pre>
      </div>
    </div>
  )
}
