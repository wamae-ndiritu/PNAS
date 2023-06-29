export const reducer = (state, action) => {
  if (action.type === "GET_ADVICE_SUCCESS") {
    return {
      ...state,
      item: action.payload,
      isModalOpen: true,
    };
  } else if (action.type === "CLOSE_MODAL") {
    return {
      ...state,
      isModalOpen: false,
    };
  }
};
