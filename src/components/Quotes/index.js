import React from 'react';
import './Quotes.css';

function Quotes({item}) {
    return (
        <div className="quote">
            <span className="text">
                {item.quote} <br />
            </span>
            <span>
                by 
                <a href="">
                    <small className="author">
                        {item.author.author}
                    </small>
                </a>
            </span>
            <div className="tags">
                Tags:
                {item.tags.map((tag, key)=>(
                    // console.log(tag)
                    <a class="tag" href={`/tag/change/page/${tag}/`} key={key}>{tag.tag} </a>
                ))}
            </div>
        </div>
    )
}

export default Quotes
