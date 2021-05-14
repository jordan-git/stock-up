import { Fragment } from 'react';
import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom';
import './App.css';

function App() {
  const Home = () => (
    <Fragment>
      <h1>Home</h1>
    </Fragment>
  );

  const About = () => (
    <Fragment>
      <h1>About</h1>
    </Fragment>
  );

  const Contact = () => (
    <Fragment>
      <h1>Contact</h1>
    </Fragment>
  );

  return (
    <Router>
      <header>
        <div id="title">
          <h1>StockUp</h1>
        </div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
            <li>
              <Link to="/contact">Contact</Link>
            </li>
          </ul>
        </nav>
      </header>
      <main>
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/about" exact component={About} />
          <Route path="/contact" exact component={Contact} />
        </Switch>
      </main>
      <footer>Copyright</footer>
    </Router>
  );
}

export default App;
