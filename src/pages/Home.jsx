import HomeAbout from "../components/HomeAbout";
import HomeFeatures from "../components/HomeFeatures";
import HomeHero from "../components/HomeHero";

const Home = () => {
  return (
    <div style={{marginTop: '80px'}}>
      <div className="hero">
        <HomeHero />
      </div>
      <div className="about-container">
        <HomeAbout />
      </div>
      <div className="features-container">
        <HomeFeatures />
      </div>
    </div>
  );
};

export default Home;
