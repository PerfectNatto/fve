import { useState } from 'react';
import Switch from '@mui/material/Switch';

export default function CustomSwitch() {
  const [checked, setChecked] = useState(false);

  const handleToggle = (event: React.ChangeEvent<HTMLInputElement>) => {
    const nextChecked = event.target.checked;

    setChecked(nextChecked);

    // ここにtoggle時に実行したい処理を書く
    console.log('toggle:', nextChecked);
  };

  return (
    <Switch
      checked={checked}
      onChange={handleToggle}
      disableRipple
      sx={{
        width: 72,
        height: 44,
        padding: 0,

        '& .MuiSwitch-switchBase': {
          padding: '6px',
          transitionDuration: '200ms',

          '&.Mui-checked': {
            transform: 'translateX(28px)',
            color: '#fff',

            '& + .MuiSwitch-track': {
              backgroundColor: '#7c3aed', // checked時の色
              opacity: 1,
            },
          },
        },

        '& .MuiSwitch-thumb': {
          width: 32,
          height: 32,
          boxShadow: '0 3px 10px rgba(0, 0, 0, 0.25)',
        },

        '& .MuiSwitch-track': {
          borderRadius: 44 / 2,
          backgroundColor: '#d1d5db', // 後ろのグレー
          opacity: 1,
        },
      }}
    />
  );
}
