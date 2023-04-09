import { Container, Navbar, Nav } from "react-bootstrap";
import { Link, useNavigate } from "react-router-dom";
import igIcon from "../assets/images/instagram-icon.webp";
import waIcon from "../assets/images/whatsapp-icon.png";

const NavigationBar = () => {
  const navigate = useNavigate();

  return (
    <Navbar bg="warning" expand="lg" fixed="top">
      <Container>
        <Link to="/" className="navbar-brand-custom">
          Recogni Pilajara
        </Link>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="mx-auto">
            <div className="nav-item-container">
              <Nav.Link as={Link} to="/" className="nav-link-custom">
                Home
              </Nav.Link>
            </div>
            <div className="nav-item-container">
              <Nav.Link as={Link} to="/attendinfo" className="nav-link-custom">
                Attendance Info
              </Nav.Link>
            </div>
            <div className="nav-item-container">
              <Nav.Link as={Link} to="/topic" className="nav-link-custom">
                Topic
              </Nav.Link>
            </div>
          </Nav>
          <Nav>
            <Nav.Link href="#" className="nav-link-custom">
              <img alt="Instagram" src={igIcon} className="social-icon" />
            </Nav.Link>
            <Nav.Link href="#" className="nav-link-custom">
              <img alt="WhatsApp" src={waIcon} className="social-icon" />
            </Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default NavigationBar;
