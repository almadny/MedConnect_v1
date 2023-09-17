import React from 'react'

function HowItWorks() {
  const steps = [
    {
      title: 'Step 1: Sign Up',
      description: 'Create an account on our platform.',
    },
    {
      title: 'Step 2: Schedule Appointment',
      description: 'Select a suitable date and time for your consultation.',
    },
    {
      title: 'Step 3: Consultation',
      description: 'Connect with your healthcare provider through video call.',
    },
  ];

  return (
    <section className="bg-gray-100 py-16">
      <div className="container mx-auto">
        <h2 className="text-3xl font-semibold text-center text-gray-800 mb-8">
          How It Works
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {steps.map((step, index) => (
            <div
              key={index}
              className="bg-white rounded-lg shadow-lg p-6 text-center"
            >
              <h3 className="text-xl font-semibold text-gray-800 mb-4">
                {step.title}
              </h3>
              <p className="text-gray-600">{step.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default HowItWorks;
