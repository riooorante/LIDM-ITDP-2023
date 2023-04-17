import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import AttendInfo from "./pages/AttendInfo";
import Topic from "./pages/Topic";
import StudentInfo from "./pages/StudentInfo";

// import StudentInformation from "./pages/EditData";
// import './style/EditData.css'

import NavigationBar from "./components/NavigationBar";
import Footer from "./components/Footer";

import "./App.css";
import "./style/NavigationBar.css";
import "./style/HomeHero.css";
import "./style/HomeAbout.css";
import "./style/HomeFeatures.css";
import "./style/Footer.css";
import "./style/AttendData.css";
import "./style/Loader.css";
import './style/StudentData.css'

const App = () => {
  return (
    <Router>
      <NavigationBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/attendinfo" element={<AttendInfo />} />
        <Route path="/topic" element={<Topic />} />
        <Route
          path="/attendinfo/studentinformation"
          element={<StudentInfo />}
        />
      </Routes>
      <div className="footer-container">
        <Footer />
      </div>
    </Router>
  );
};

export default App;
