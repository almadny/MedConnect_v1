import React, {useContext} from 'react'
import GeneralContext from './GeneralContext';

export function useAuth() {
  const context = useContext(GeneralContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}