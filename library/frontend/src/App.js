import React from 'react';
// import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js';
// import axios from 'axios';



class App extends React.Component {
    constructor(props) {
        super(props)
        const author1 = {id: 1, first_name: 'Грин', birth_year: 1880}
        const author2 = {id: 2, first_name: 'Пушкин', birth_year: 1799}
        const authors = [author1, author2]
        this.state = {
            'authors': authors
        }


    }

//    componentDidMount() {
//        axios.get('http://127.0.0.1:8000/api/authors/')
//            .then(response => {
//                const authors = response.data
//                    this.setState(
//                        {
//                            'authors': authors
//                        }
//                    )
//            }).catch(error => console.log(error))
//    }


    render () {
        return (
           <div className="App">
                <AuthorList items={this.state.authors} />
           </div>

        )
    }
}

export default App;

