import { Col, Container, Row } from "react-bootstrap";

const HomeHero = () => {
  return (
    <div className="hero-text">
      <Container className="text-white d-flex justify-content-center align-items-center text-center">
        <Row>
          <Col>
            <div className="hero-title">Welcome to</div>
            <div className="hero-title">
              <i>Recogni Pilajara'</i>
            </div>
          </Col>
        </Row>
      </Container>
    </div>
  );
};

export default HomeHero;
