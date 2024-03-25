import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import CustomerList from "./CustomerList";
import NewCustomerModal from "./NewCustomerModal";

import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
  state = {
    customers: []
  };

  componentDidMount() {
    this.resetState();
  }

  getCustomers = () => {
    axios.get(API_URL).then(res => this.setState({ customers: res.data }));
  };

  resetState = () => {
    this.getCustomers();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <CustomerList
              customers={this.state.customers}
              resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
          <Col>
            <NewCustomerModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;