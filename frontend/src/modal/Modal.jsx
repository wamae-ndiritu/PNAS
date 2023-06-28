import React, { useEffect, useState } from "react";
import "./Modal.css"; // Import your modal styles

function Modal({ isModalOpen }) {
  const [modalOpen, setModalOpen] = useState(isModalOpen);

  const closeModal = () => {
    setModalOpen(false);
    document.body.style.overflow = "auto"; // Allow scrolling on the body
  };

  useEffect(() => {
    if (modalOpen) {
      document.body.style.overflow = "hidden"; // Prevent scrolling on the body
    }
  });

  return (
    <div>
      {modalOpen && (
        <div className="modal-overlay">
          <div className="modal-content">
            <h4>Nutritional Advice</h4>
            <h5>Weight Status: Normal Weight</h5>
            <p className="alert alert-success">
              You have a healthy weight. Maintain a balanced diet and exercise
              regularly.
            </p>
            <h6>Foods to include:</h6>
            <ul>
              <li>
                Whole grains (e.g., quinoa, brown rice, whole wheat bread)
              </li>
              <li>Lean proteins (e.g., chicken, fish, beans)</li>
              <li>Healthy fats (e.g., avocado, nuts, seeds)</li>
              <li>Dairy or dairy alternatives (e.g., milk, yogurt, tofu)</li>
              <li>Colorful fruits and vegetables</li>
            </ul>
            <button onClick={closeModal}>Close Modal</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Modal;
