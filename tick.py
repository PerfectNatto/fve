 appearance: none;
  -webkit-appearance: none;

  width: 20px;
  height: 20px;
  margin: 0;

  border: 2px solid #767676;
  border-radius: 4px;
  background-color: #fff;
  cursor: pointer;

  display: inline-grid;
  place-content: center;

  &::before {
    content: "";
    width: 10px;
    height: 6px;
    border-left: 2px solid #fff;
    border-bottom: 2px solid #fff;
    transform: rotate(-45deg) scale(0);
    transform-origin: center;
  }

  &:checked {
    background-color: #006adc;
    border-color: #006adc;
  }

  &:checked::before {
    transform: rotate(-45deg) scale(1);
  }
