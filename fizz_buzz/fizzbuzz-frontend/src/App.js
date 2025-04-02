import React, {useState} from 'react';

function App(){
  const[number, setNumber] = useState('');
  const[result, setResult] = useState([]);


  const handleSubmit = async (event) => {
    event.preventDefault();

    const response = await fetch('http://127.0.0.1:8000/api/fizzbuzz/', {
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ number })
    });
    

    const data = await response.json();
    setResult(data.result|| []);
  };

  return (
    <div className="app">
      <h1>Fizz BUzz Generator</h1>


      <form onSubmit={handleSubmit}>
        <input
          type="number"
          value={number}
          onChange={(event) => setNumber(event.target.value)}
          placeholder="Enter a number for the 'Fizz Buzz' reaction"
          required
        />
        <button type="submit">Generate</button>
      </form>

      <ul>
        {result.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
}


export default App;
