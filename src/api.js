const URL_BASE = 'http://127.0.0.1:8000/';
const getQuotes = async () => {
    let url = `${URL_BASE}quotes/`;
    const res = await fetch(url);
    const quotes = await res.json();
    return quotes;
}

export default getQuotes;