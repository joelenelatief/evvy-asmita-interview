import React, { useEffect, useState } from "react";
import Layout from "../components/layout";
import { testsService } from "../services/testsService";
import { AxiosError } from "axios";

type TestResult = {
  barcode: string;
  patient_name: string;
  is_positive: boolean;
}

const TestResults = ({}: {}) => {
  const [results, setResults] = useState<TestResult[]>([]);
  const [error, setError] = useState<AxiosError | null>(null);

  useEffect(() => {
    const fetchTestResults = () => {
      testsService.fetchTestResults({
        onSuccess: (response: {data: TestResult[]}) => {
          setResults(response.data);
        },
        onFailure: (error: AxiosError) => {
          setError(error)
        }
      });
    };
    fetchTestResults();
  }, []);

  return (
    <Layout title="Test Results">
      <div>
        {results?.map((result) => (
          <div key={result.barcode}>
            {result.patient_name}{" - "}
            {String(result.is_positive)}
          </div>
        ))}
      </div>
    </Layout>
  );
};

export default TestResults;
