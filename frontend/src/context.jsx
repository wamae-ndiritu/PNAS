import React, { createContext, useContext, useReducer } from "react";
import { defaultState, reducer } from "./reducer";

const initialState = {
  item: {},
  isModalOpen: false,
};

// Create the context object
const AppContext = createContext();

// Create a custom provider component that wraps the AppContext.Provider
const AppProvider = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, initialState);

  const getAdviceSuccess = (data) => {
    dispatch({ type: "GET_ADVICE_SUCCESS", payload: data });
  };

  const closeModal = () => {
    dispatch({ type: "CLOSE_MODAL" });
  };

  return (
    <AppContext.Provider value={{ ...state, getAdviceSuccess, closeModal }}>
      {children}
    </AppContext.Provider>
  );
};

export const useGlobalContext = () => {
  return useContext(AppContext);
};

export { AppContext, AppProvider };
