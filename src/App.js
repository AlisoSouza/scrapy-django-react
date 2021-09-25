import Quotes from "./components/Quotes";
import React, {useEffect, useState} from "react";
import getQuotes from "./api.js"
function App() {

    const [quotes, setQuotes] = useState([]);
    useEffect(()=>{
        const allquotes = async () => {
            let all_quotes = await getQuotes();
            setQuotes(all_quotes);
            console.log(all_quotes);
        }
        allquotes();
    }, []);



  return (
    <div className="App">
      <div className="container">
        <div className="row header-box">
          <div className="col-md-8">
            <h1>
              <a href="">Quotes to Scrape</a>
            </h1>
          </div>
        </div>
        <div className="row">
          <div className="col-md-8">
            {quotes.map((item, key)=>(
              <Quotes key={key} item={item}></Quotes>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
