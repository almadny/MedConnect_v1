import React from 'react';

const FAQ = () => {
  const faqs = [
    {
      question: 'What is telemedicine?',
      answer: 'Telemedicine is the remote diagnosis and treatment of patients through telecommunications technology.'
    },
    {
      question: 'How can I schedule a telemedicine appointment?',
      answer: 'You can schedule a telemedicine appointment by visiting our website and filling out the appointment request form.'
    },
    {
      question: 'Is telemedicine covered by insurance?',
      answer: 'Coverage for telemedicine services varies by insurance provider. Please check with your insurance company to determine your coverage.'
    },
    {
      question: 'What equipment do I need for a telemedicine appointment?',
      answer: 'You will need a device with a camera and microphone, such as a smartphone, tablet, or computer, and a stable internet connection.'
    },
    {
      question: 'Are telemedicine appointments secure?',
      answer: 'Yes, we use secure and encrypted technology to ensure the privacy and security of your telemedicine appointments.'
    }
  ];

  return (
    <div className="container mx-auto py-8">
      <h2 className="text-3xl font-semibold mb-4">Frequently Asked Questions</h2>
      <ul>
        {faqs.map((faq, index) => (
          <li key={index} className="mb-4">
            <div className="bg-white rounded shadow p-4">
              <h3 className="text-lg font-semibold mb-2">{faq.question}</h3>
              <p>{faq.answer}</p>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FAQ;
