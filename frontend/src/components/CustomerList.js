import React, { Component } from "react";
import { Table } from "reactstrap";
import NewCustomerModal from "./NewCustomerModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

class CustomerList extends Component {
  render() {
    const customers = this.props.customers;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Document</th>
            <th>Phone</th>
            <th>Registration</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!customers || customers.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, no one here yet</b>
              </td>
            </tr>
          ) : (
            customers.map(customer => (
              <tr key={customer.pk}>
                <td>{customer.name}</td>
                <td>{customer.email}</td>
                <td>{customer.document}</td>
                <td>{customer.phone}</td>
                <td>{customer.registrationDate}</td>
                <td align="center">
                  <NewCustomerModal
                    create={false}
                    customer={customer}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    pk={customer.pk}
                    resetState={this.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default CustomerList;