import React, { useEffect, useReducer, useState } from "react";
import "./Modal.css"; // Import your modal styles
import { useGlobalContext } from "../context";

function Modal() {
  const { item, isModalOpen, closeModal } = useGlobalContext();

  const handleCloseModal = () => {
    closeModal();
    document.body.style.overflow = "auto"; // Allow scrolling on the body
  };

  console.log(item);

  return (
    <div>
      {isModalOpen && (
        <div className="modal-overlay">
          <div className="modal-content">
            <h4>Nutritional Advice</h4>
            <h5>Weight Status: {item.status}</h5>
            <p
              className={
                item.status === "normal weight"
                  ? `alert alert-success`
                  : `alert alert-warning`
              }
            >
              {item.comment}
            </p>
            <h6>Foods to include:</h6>
            <ul>
              {item.items.map((newItem) => {
                const { id, item } = newItem;
                return <li key={id}>{item}</li>;
              })}
            </ul>
            {item.goalItems.map((goalItem) => {
              const { id, title, items } = goalItem;
              return (
                <div key={id}>
                  <h6>Foods for {title}:</h6>
                  <ul>
                    {items.map((newItem) => {
                      const { id, item } = newItem;
                      return <li key={id}>{item}</li>;
                    })}
                  </ul>
                </div>
              );
            })}
            <button onClick={handleCloseModal}>Close Modal</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Modal;
